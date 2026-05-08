# KnitResult Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~KnitResult`

Gets or sets whether to knit the bodies created by deleting original faces in an extruded surface.
Gets or sets whether to knit the bodies created by deleting original faces in an extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KnitResult As System.Boolean
```

```

Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean
 
instance.KnitResult = value
 
value = instance.KnitResult
```

```

System.bool KnitResult {get; set;}
```

```

property System.bool KnitResult {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to knit the bodies created by deleting original faces, false to not (see **Remarks**)

Remarks

This property is only available if:

- [ISurfExtrudeFeatureData::BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.md) = false.
- [ISurfExtrudeFeatureData::DeleteOriginalFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~DeleteOriginalFace.md) = true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)
