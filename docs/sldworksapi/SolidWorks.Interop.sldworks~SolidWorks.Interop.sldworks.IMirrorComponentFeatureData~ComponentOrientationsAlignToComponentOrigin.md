# ComponentOrientationsAlignToComponentOrigin Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin`

Gets or sets the array of orientations for the components whose axes align to origins.
Gets or sets the array of orientations for the components whose axes align to origins.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ComponentOrientationsAlignToComponentOrigin As System.Object
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Object
 
instance.ComponentOrientationsAlignToComponentOrigin = value
 
value = instance.ComponentOrientationsAlignToComponentOrigin
```

```

System.object ComponentOrientationsAlignToComponentOrigin {get; set;}
```

```

property System.Object^ ComponentOrientationsAlignToComponentOrigin {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [swMirrorComponentOrientation2\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentOrientation2_e.html) values

Remarks

There is a one-to-one mapping between this array and [IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.md). If there are fewer elements in this array than are in IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin, then missing orientations default to swMirrorComponentOrientation2\_e.swOrientation\_MirroredX\_MirroredY.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
