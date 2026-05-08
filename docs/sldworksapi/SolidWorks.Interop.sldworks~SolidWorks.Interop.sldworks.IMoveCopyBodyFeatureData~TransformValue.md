# TransformValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformValue`

Gets or sets the distance or angle by which to move or rotate the selected bodies based on the selected edge.
Gets or sets the distance or angle by which to move or rotate the selected bodies based on the selected edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransformValue As System.Double
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double
 
instance.TransformValue = value
 
value = instance.TransformValue
```

```

System.double TransformValue {get; set;}
```

```

property System.double TransformValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance in meters or angle in radians

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)
