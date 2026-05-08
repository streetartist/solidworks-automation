# FeatureScope Property (IThickenFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScope`

Gets or sets whether to use scope for the thicken feature in a multibody part.
Gets or sets whether to use scope for the thicken feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureScope As System.Boolean
```

```

Dim instance As IThickenFeatureData
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

- true, only the specified bodies in the multibody part are affected by the thicken feature
- false, all of the bodies in the multibody part are affected by the thicken feature

Remarks

The thicken feature is expanded along the plane on which the feature is created and affects all or only the specified bodies it intersects.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md)  
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.md)  
[IThickenFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~GetFeatureScopeBodiesCount.md)  
[IThickenFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~IGetFeatureScopeBodies.md)  
[IThickenFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~ISetFeatureScopeBodies.md)  
[IThickenFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~AutoSelect.md)  
[IThickenFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScopeBodies.md)
