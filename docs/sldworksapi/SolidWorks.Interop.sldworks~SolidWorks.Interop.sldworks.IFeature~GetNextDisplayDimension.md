# GetNextDisplayDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension`

Gets the next display dimension associated with this feature.
Gets the next display dimension associated with this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNextDisplayDimension( _
   ByVal DispIn As System.Object _
) As System.Object
```

```

Dim instance As IFeature
Dim DispIn As System.Object
Dim value As System.Object
 
value = instance.GetNextDisplayDimension(DispIn)
```

```

System.object GetNextDisplayDimension( 
   System.object DispIn
)
```

```

System.Object^ GetNextDisplayDimension( 
   System.Object^ DispIn
) 
```

#### Parameters

*DispIn*
:   [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object obtained with [IFeature::GetFirstDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.md) or from your previous call to this method

#### Return Value

Next [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object based on the DispIn argument, or NULL if there are no more dimensions

Remarks

Before you can get a feature's IDisplayDimension, use [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.md) and swDisplayFeatureDimension to display them.

All dimensions on this feature and its sub-features are returned by either [IFeature::GetFirstDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.md) and IFeature::GetNextDisplayDimension or [IFeature::EnumDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~EnumDisplayDimensions.md). In the user-interface, this is equivalent to double-clicking a feature in the FeatureManager design tree to display all of the feature and sub-feature dimensions.

If you call this method from a sub-feature (for example, the sketch of a boss-extrude), then the IDisplayDimension object returned by IFeature::GetFirstDisplayDimension and IFeature::GetNextDisplayDimension contain only the dimensions found in the sketch.

This method might not always return display dimensions in the same order.

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
