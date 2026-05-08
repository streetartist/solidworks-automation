# AddHoleCallout2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2`

Adds a hole callout at the specified position to the hole whose edge is selected.
Adds a hole callout at the specified position to the hole whose edge is selected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddHoleCallout2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.AddHoleCallout2(X, Y, Z)
```

```

System.object AddHoleCallout2( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ AddHoleCallout2( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X position of hole callout in meters

*Y*
:   Y position of hole callout in meters

*Z*
:   Z position of hole callout in meters

#### Return Value

[Display dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) representing the hole callout

Remarks

When you call this method, the user must click OK in the dialog that shows the system-generated hole callout.

Example

'VBA

'---------------------------------------------------------  
' This example shows how to add a hole callout to  
' a hole in a drawing.  
'  
' Preconditions:  
' 1. Open the drawing of a part that contains a hole.  
' 2. Select the edge of the hole where to add the callout in the graphics area.  
' 3. Open the Immediate window.  
'  
' Postconditions:  
' 1. A hole callout is added to the hole in the drawing.  
' 2. Examine the drawing and Immediate window to verify.  
' 3. Close the drawing without saving any changes.  
'  
' Tested using SolidWorks 2011 SP1.  
'-----------------------------------------------------------

Option Explicit

Const Xpos                      As Double = 0.165  
Const Ypos                      As Double = 0.435  
Const Zpos                      As Double = 0#

Sub main()  
    Dim swApp                   As SldWorks.SldWorks  
    Dim swModel                 As SldWorks.ModelDoc2  
    Dim swModelDocExt           As SldWorks.ModelDocExtension  
    Dim swDraw                  As SldWorks.DrawingDoc  
    Dim swDispDim               As SldWorks.DisplayDimension  
    Dim swAnn                   As SldWorks.Annotation  
    Dim status                  As Boolean  
    Dim annType                 As Long  
     
    Set swApp = CreateObject("SldWorks.Application")  
    Set swModel = swApp.ActiveDoc  
    Set swModelDocExt = swModel.Extension  
    Set swDraw = swModel

    status = swDraw.ActivateView("Drawing View1")  
    ' Select the edge of the hole where to add the callout  
    ' status = swModelDocExt.SelectByID2("", "EDGE", 0.6280838894175, 0.4565734807731, -499.9234340021, False, 0, Nothing, 0)  
    Set swDispDim = swDraw.**AddHoleCallout2**(Xpos, Ypos, Zpos)  
     
    Debug.Print "All          = " + swDispDim.GetText(swDimensionTextAll)  
    Debug.Print "Prefix       = " + swDispDim.GetText(swDimensionTextPrefix)  
    Debug.Print "Suffix       = " + swDispDim.GetText(swDimensionTextSuffix)  
    Debug.Print "CalloutAbove = " + swDispDim.GetText(swDimensionTextCalloutAbove)  
    Debug.Print "CalloutBelow = " + swDispDim.GetText(swDimensionTextCalloutBelow)  
     
    Set swAnn = swDispDim.GetAnnotation  
     
    annType = swAnn.GetType  
    Debug.Print "Annotation Type      = " + Str(annType)  
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::IAddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.md)  
[IDisplayDimension::IsHoleCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md)  
[IDisplayDimension::GetHoleCalloutVariables Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.md)
