# FixedAxisOfRotation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation`

Gets or sets whether patterned instances rotate around a common axis.
Gets or sets whether patterned instances rotate around a common axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedAxisOfRotation As System.Boolean
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean
 
instance.FixedAxisOfRotation = value
 
value = instance.FixedAxisOfRotation
```

```

System.bool FixedAxisOfRotation {get; set;}
```

```

property System.bool FixedAxisOfRotation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if patterned instances rotate around [ILocalLinearPatternFeatureData::RotationAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAxis.md), false if each instance rotates about its own axis

Remarks

This property is valid only if [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.md) is true.

If this property is set to:

- True, then you can also specify [ILocalLinearPatternFeatureData::AlignToSeed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~AlignToSeed.md).
- False, then the rotation axis of each instance of a component is translated along Direction 1 and then rotated following the axis of rotation for that component.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)
