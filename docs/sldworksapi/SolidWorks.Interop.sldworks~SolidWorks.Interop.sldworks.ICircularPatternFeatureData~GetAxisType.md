# GetAxisType Method (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetAxisType`

Gets the type of geometry used to determine the direction of this circular pattern.
Gets the type of geometry used to determine the direction of this circular pattern.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAxisType() As System.Integer
```

```

Dim instance As ICircularPatternFeatureData
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

Geometry type used to create the circular pattern:

- 0 = reference axis
- 1 = edge
- 2 = dimension
- 3 = sketch line

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[ICircularPatternFeatureData::Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis.md)
