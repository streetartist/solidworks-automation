# GetEnvironment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetEnvironment`

Gets the IEnvironment object.
Gets the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEnvironment() As System.Object
```

```

Dim instance As ISldWorks
Dim value As System.Object
 
value = instance.GetEnvironment()
```

```

System.object GetEnvironment()
```

```

System.Object^ GetEnvironment(); 
```

#### Return Value

[IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) object

Remarks

All numeric values returned from the IEnvironment object are relative to a unit text height of 1.0.; i.e., if a symbol has a text height of 0.15, then multiply the numeric values returned by 0.15.

Example

[Analyze Text and Geometry in GTol Symbol (C#)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_CSharp.htm)  
[Analyze Text and Geometry in GTol Symbol (VB.NET)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VBNET.htm)  
[Analyze Text and Geometry in GTol Symbol (VBA)](Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetEnvironment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetEnvironment.md)
