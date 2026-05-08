# CheckFeatureUse Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~CheckFeatureUse`

Checks to see if this sketch is valid for use in creating a specified feature.
Checks to see if this sketch is valid for use in creating a specified feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CheckFeatureUse( _
   ByVal FeatureType As System.Integer, _
   ByRef OpenCount As System.Integer, _
   ByRef ClosedCount As System.Integer _
) As System.Integer
```

```

Dim instance As ISketch
Dim FeatureType As System.Integer
Dim OpenCount As System.Integer
Dim ClosedCount As System.Integer
Dim value As System.Integer
 
value = instance.CheckFeatureUse(FeatureType, OpenCount, ClosedCount)
```

```

System.int CheckFeatureUse( 
   System.int FeatureType,
   out System.int OpenCount,
   out System.int ClosedCount
)
```

```

System.int CheckFeatureUse( 
   System.int FeatureType,
   [Out] System.int OpenCount,
   [Out] System.int ClosedCount
) 
```

#### Parameters

*FeatureType*
:   Determine if this type of feature can be created as defined in [swSketchCheckFeatureProfileUsage\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchCheckFeatureProfileUsage_e.html)

*OpenCount*
:   Number of open contours found in this sketch

*ClosedCount*
:   Number of closed contours found in this sketch

#### Return Value

swSketchCheckFeatureStatus\_OK if this sketch can be used to create the specified feature; see [swSketchCheckFeatureStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchCheckFeatureStatus_e.html) for possible failure values

Remarks

This method is equivalent to the SOLIDWORKS interactive tool Check Sketch for Feature Usage. See the SOLIDWORKS Help for details.

The OpenCount and ClosedCount arguments are output values. If this method returns swSketchCheckFeatureStatus\_OK, meaning that the sketch can be used to create the specified feature, then these two arguments contain useful information. If this method returns something else, then OpenCount and ClosedCount both return 0.

If the featureType value is not valid, this method returns  swSketchCheckFeatureStatus\_UnknownError.

Example

[Determine If Sketch Suitable for Feature (VBA)](Determine_If_Sketch_Suitable_for_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
