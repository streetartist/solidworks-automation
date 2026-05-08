# DeleteOriginalFace Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~DeleteOriginalFace`

Gets or sets whether to delete the original faces of this extruded surface.
Gets or sets whether to delete the original faces of this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DeleteOriginalFace As System.Boolean
```

```

Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean
 
instance.DeleteOriginalFace = value
 
value = instance.DeleteOriginalFace
```

```

System.bool DeleteOriginalFace {get; set;}
```

```

property System.bool DeleteOriginalFace {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to delete the original faces, false to not (see **Remarks**)

Remarks

This property is only available if [ISurfExtrudeFeatureData::BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.md) = false.

Deleting original faces results in the model being hollow where the faces were deleted and creates multiple bodies. To create a single body when original faces are deleted, use [ISurfExtrudeFeatureData::KnitResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~KnitResult.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)
