# MirrorType Property (IMirrorComponentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorType`

Gets or sets the mirror position.
Gets or sets the mirror position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorType As System.Integer
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Integer
 
instance.MirrorType = value
 
value = instance.MirrorType
```

```

System.int MirrorType {get; set;}
```

```

property System.int MirrorType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of mirror as defined by [swMirrorComponentMirrorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentMirrorType_e.html)

Remarks

If not explicitly set, this property defaults to swMirrorComponentMirrorType\_e.swMirrorType\_CenterOfBoundingBox.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
