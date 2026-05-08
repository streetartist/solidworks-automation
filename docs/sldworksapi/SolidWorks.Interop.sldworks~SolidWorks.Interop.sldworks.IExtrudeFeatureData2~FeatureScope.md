# FeatureScope Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScope`

Gets or sets whether to use scope for the extrude feature in a multibody part.
Gets or sets whether to use scope for the extrude feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureScope As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.FeatureScope = value
 
value = instance.FeatureScope
```

```

System.bool FeatureScope {get; set;}
```

```

property System.bool FeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

When:

- true, only the specified bodies in the multibody part are affected by the extrude feature
- false, all of the bodies in the multibody part are affected by the extrude feature

Remarks

The extrude feature is expanded along the plane on which the feature is created and affects all or only the specified bodies it intersects.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.md)  
[IExtrudeFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.md)  
[IExtrudeFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFeatureScopeBodiesCount.md)  
[IExtrudeFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetFeatureScopeBodies.md)  
[IExtrudeFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFeatureScopeBodies.md)
