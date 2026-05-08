# GetFirstDisplayDimension Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension`

Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature.
Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstDisplayDimension() As System.Object
```

```

Dim instance As IFeature
Dim value As System.Object
 
value = instance.GetFirstDisplayDimension()
```

```

System.object GetFirstDisplayDimension()
```

```

System.Object^ GetFirstDisplayDimension(); 
```

#### Return Value

First [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object for this feature, or Nothing or null if there are no dimensions for this feature

Remarks

Before you can get a feature's IDisplayDimension, use [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.md) and swDisplayFeatureDimensions to display them.

All dimensions on this feature its sub-features are returned by either IFeature::GetFirstDisplayDimension and [IFeature::GetNextDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension.md) or [IFeature::EnumDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~EnumDisplayDimensions.md). In the user-interface, this is equivalent to double-clicking a feature in the FeatureManager design tree to display all of the feature and sub-feature dimensions.

If you call this method from a sub-feature (for example, the sketch of a boss-extrude), then the IDisplayDimension object returned by IFeature::GetFirstDisplayDimension and IFeature::GetNextDisplayDimension contain only the dimensions found in the sketch.

Do not use [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Visible.md) property to modify this method's return value.

This method might not return the same display dimension every time it is called.

Example

[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)  
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)  
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension.md)
