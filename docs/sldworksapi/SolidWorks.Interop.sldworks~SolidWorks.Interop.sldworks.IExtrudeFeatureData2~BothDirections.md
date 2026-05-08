# BothDirections Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~BothDirections`

Gets or sets whether the extrusion is in both directions.
Gets or sets whether the extrusion is in both directions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BothDirections As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.BothDirections = value
 
value = instance.BothDirections
```

```

System.bool BothDirections {get; set;}
```

```

property System.bool BothDirections {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if extrusion is in both directions, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)
