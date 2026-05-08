# AutoSelect Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect`

Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part.
Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSelect As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.AutoSelect = value
 
value = instance.AutoSelect
```

```

System.bool AutoSelect {get; set;}
```

```

property System.bool AutoSelect {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically select all bodies, false to select specific bodies for [IExtrudeFeatureData2::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.md) and [IExtrudeFeatureData2::ISetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFeatureScopeBodies.md)

Remarks

This property is only available when the [IExtrudeFeatureData2::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScope.md) property is true. The extrude feature is expanded along the plane on which the feature is created and selects all or only the specified bodies it intersects.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFeatureScopeBodiesCount.md)  
[IExtrudeFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetFeatureScopeBodies.md)
