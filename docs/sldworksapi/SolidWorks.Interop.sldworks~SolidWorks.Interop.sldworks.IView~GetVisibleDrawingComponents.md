# GetVisibleDrawingComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents`

Gets all of the unobscured drawing components in this drawing view of an assembly drawing.
Gets all of the unobscured drawing components in this drawing view of an assembly drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleDrawingComponents() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetVisibleDrawingComponents()
```

```

System.object GetVisibleDrawingComponents()
```

```

System.Object^ GetVisibleDrawingComponents(); 
```

#### Return Value

Visible [IDrawingComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)s in this drawing view

Remarks

Visible components are components not completely obscured by other components in the view.

After calling this method to retrieve the visible drawing components, use [IDrawingComponent::Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Component.md) to get a component object that fully supports all of the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) methods and properties.

Example

'VBA

'--------------------------------------------------------------------  
' Preconditions:  
' 1. Open a drawing document of an assembly that contains **Drawing View1**  
'     with one or more visible drawing components.  
' 2. Open the Immediate window.  
'  
' Postconditions:  
' 1. Gets the visible drawing components and their names.  
' 2. Examine the Immediate window.  
'-------------------------------------------------------  
Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim swView As SldWorks.View  
Dim swDrComp As SldWorks.DrawingComponent  
Dim swComp As Component2  
Dim vComps As Variant  
Dim vBodies As Variant  
Dim boolstatus As Boolean  
Dim itr As Long

Sub main()  
   
    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
    Set swModelDocExt = swModel.Extension  
    Set swSelMgr = swModel.SelectionManager  
    boolstatus = swModel.ActivateView("Drawing View1")  
    boolstatus = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)  
    Set swView = swSelMgr.GetSelectedObject6(1, -1)  
    swModel.ClearSelection2 True  
     
    'Get all visible components in Drawing View1  
    vComps = swView.**GetVisibleDrawingComponents**  
     
    'Print the number of visible components  
    Debug.Print "Number of components:"  
    Debug.Print "  " & UBound(vComps) + 1  
     
    'Iterate through the visible components and print each one's name  
    Debug.Print "Names of drawing view components and the referenced assembly component names:"  
    For itr = 0 To UBound(vComps)  
        Debug.Print ""  
        Set swDrComp = vComps(itr)  
        Debug.Print "  " & swDrComp.Name  
        Set swComp = swDrComp.Component  
        'Print the referenced assembly component name  
        If Not swComp Is Nothing Then  
             Debug.Print "    " & swComp.Name2  
             Call swComp.GetBodies3(swAllBodies, vBodies)  
        End If  
    Next itr  
   
End Sub

Example

[Get Visible Drawing Components (VB.NET)](Get_Visible_Drawing_Components_Example_VBNET.htm)  
[Get Visible Drawing Components (C#)](Get_Visible_Drawing_Components_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::GetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.md)
