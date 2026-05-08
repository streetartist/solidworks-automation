# GetHoleCalloutVariables Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables`

Gets access to hole callout variables in a hole callout.
Gets access to hole callout variables in a hole callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHoleCalloutVariables() As System.Object
```

```

Dim instance As IDisplayDimension
Dim value As System.Object
 
value = instance.GetHoleCalloutVariables()
```

```

System.object GetHoleCalloutVariables()
```

```

System.Object^ GetHoleCalloutVariables(); 
```

#### Return Value

Array of [CalloutVariable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md) objects

Example

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)  
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)  
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.md)  
[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.md)  
[ICalloutStringVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.md)  
[IDisplayDimension::IsHoleCallout Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md)  
[IDrawingDoc::AddHoleCallout2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.md)  
[IDrawingDoc::IAddHoleCallout2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.md)
