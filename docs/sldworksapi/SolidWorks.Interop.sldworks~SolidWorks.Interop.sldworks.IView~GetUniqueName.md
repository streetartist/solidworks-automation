# GetUniqueName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUniqueName`

Gets the unique name of this section view.
Gets the unique name of this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUniqueName() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.GetUniqueName()
```

```

System.string GetUniqueName()
```

```

System.String^ GetUniqueName(); 
```

#### Return Value

Name of this section view

Remarks

Before selecting a specific section view using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md), call this method to get the unique name of the section view in "Drawing View*number*" format.

Example

[Get Unique Name of Section View (VBA)](Get_Unique_Name_of_Section_View_Example_VB.htm)  
[Get Unique Name of Section View (VB.NET)](Get_Unique_Name_of_Section_View_Example_VBNET.htm)  
[Get Unique Name of Section View (C#)](Get_Unique_Name_of_Section_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetName2.md)
