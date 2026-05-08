# GetAxisType Method (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetAxisType`

Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature.
Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAxisType() As System.Integer
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Integer
 
value = instance.GetAxisType()
```

```

System.int GetAxisType()
```

```

System.int GetAxisType(); 
```

#### Return Value

Axis type used to create the circular pattern:

- 0 = reference axis
- 1 = edge
- 2 = dimension

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[ILocalCircularPatternFeatureData::Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Axis.md)  
[ILocalCircularPatternFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ReverseDirection.md)
