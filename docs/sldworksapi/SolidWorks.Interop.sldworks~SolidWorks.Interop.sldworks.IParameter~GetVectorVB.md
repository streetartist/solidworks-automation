# GetVectorVB Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVectorVB`

Extracts information of type vector from a parameter.
Extracts information of type vector from a parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVectorVB() As System.Object
```

```

Dim instance As IParameter
Dim value As System.Object
 
value = instance.GetVectorVB()
```

```

System.object GetVectorVB()
```

```

System.Object^ GetVectorVB(); 
```

#### Return Value

Array of 3 values in the vector (see **Remarks**)

Remarks

This method packs the data into a SafeArray in Visual Basic for Applications (VBA):

[ X,Y,Z ]

where:

|  |  |
| --- | --- |
| (double) X | x vector value stored on the parameter |
| (double) Y | y vector value stored on the parameter |
| (double) Z | z vector value stored on the parameter |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)  
[IParameter::GetVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVector.md)  
[IParameter::SetVector2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2.md)
