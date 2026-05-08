# HoleWizard2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard2`

Obsolete. Superseded by IFeatureManager::HoleWizard3.
Obsolete. Superseded by [IFeatureManager::HoleWizard3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HoleWizard2( _
   ByVal GenericHoleType As System.Integer, _
   ByVal StandardIndex As System.Integer, _
   ByVal FastenerTypeIndex As System.Integer, _
   ByVal SSize As System.String, _
   ByVal EndType As System.Short, _
   ByVal Diameter As System.Double, _
   ByVal Depth As System.Double, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal Value3 As System.Double, _
   ByVal Value4 As System.Double, _
   ByVal Value5 As System.Double, _
   ByVal Value6 As System.Double, _
   ByVal Value7 As System.Double, _
   ByVal Value8 As System.Double, _
   ByVal Value9 As System.Double, _
   ByVal Value10 As System.Double, _
   ByVal Value11 As System.Double, _
   ByVal Value12 As System.Double, _
   ByVal ThreadClass As System.String, _
   ByVal RevDir As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal AssemblyFeatureScope As System.Boolean, _
   ByVal AutoSelectComponents As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim GenericHoleType As System.Integer
Dim StandardIndex As System.Integer
Dim FastenerTypeIndex As System.Integer
Dim SSize As System.String
Dim EndType As System.Short
Dim Diameter As System.Double
Dim Depth As System.Double
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim Value3 As System.Double
Dim Value4 As System.Double
Dim Value5 As System.Double
Dim Value6 As System.Double
Dim Value7 As System.Double
Dim Value8 As System.Double
Dim Value9 As System.Double
Dim Value10 As System.Double
Dim Value11 As System.Double
Dim Value12 As System.Double
Dim ThreadClass As System.String
Dim RevDir As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim AssemblyFeatureScope As System.Boolean
Dim AutoSelectComponents As System.Boolean
Dim value As Feature
 
value = instance.HoleWizard2(GenericHoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, Diameter, Depth, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9, Value10, Value11, Value12, ThreadClass, RevDir, UseFeatScope, UseAutoSelect, AssemblyFeatureScope, AutoSelectComponents)
```

```

Feature HoleWizard2( 
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.string SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Value1,
   System.double Value2,
   System.double Value3,
   System.double Value4,
   System.double Value5,
   System.double Value6,
   System.double Value7,
   System.double Value8,
   System.double Value9,
   System.double Value10,
   System.double Value11,
   System.double Value12,
   System.string ThreadClass,
   System.bool RevDir,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents
)
```

```

Feature^ HoleWizard2( 
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.String^ SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Value1,
   System.double Value2,
   System.double Value3,
   System.double Value4,
   System.double Value5,
   System.double Value6,
   System.double Value7,
   System.double Value8,
   System.double Value9,
   System.double Value10,
   System.double Value11,
   System.double Value12,
   System.String^ ThreadClass,
   System.bool RevDir,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents
) 
```

#### Parameters

*GenericHoleType*
:   Hole type as defined in [swWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdGeneralHoleTypes_e.html)

*StandardIndex*
:   Standard property as defined in [swWzdHoleStandards\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)

*FastenerTypeIndex*
:   Screw type as defined in [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

*SSize*
:   Size of the hole

*EndType*
:   End type as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*Diameter*
:   Diameter of the hole in meters

*Depth*
:   Depth of the hole in meters

*Value1*
:   Hole-related parameter

*Value2*
:   Hole-related parameter

*Value3*
:   Hole-related parameter

*Value4*
:   Hole-related parameter

*Value5*
:   Hole-related parameter

*Value6*
:   Hole-related parameter

*Value7*
:   Hole-related parameter

*Value8*
:   Hole-related parameter

*Value9*
:   Hole-related parameter

*Value10*
:   Hole-related parameter

*Value11*
:   Hole-related parameter

*Value12*
:   Hole-related parameter

*ThreadClass*
:   One of the following thread classes:

    - 1B
    - 2B
    - 3B

    Applies to ANSI inch standard only

*RevDir*
:   True to reverse the direction of the hole, false to not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects

*AssemblyFeatureScope*
:   True if the assembly feature only affects selected bodies in the assembly, false if the assembly feature affects all bodies in the assembly

*AutoSelectComponents*
:   True to auto-select all affected components, false to only use the selected components

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

To add a hole at multiple locations, preselect the sketch points and do not specify any selection marks.

Screw Fit - As defined in [swWzdHoleScrewClearanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleScrewClearanceTypes_e.html) and only used if user does not specify a hole diameter; default value is NORMAL\_FIT

Drill Angle - defaults to 118 degrees if not specified

Input Metrics - Input angles in radians; input values in meters

Parameters for this method:

- The FastenerTypeIndex parameter has to match the standard and be valid for that hole type or an error occurs.
- The SSize parameter must be a valid size for fastener type or an error occurs.
- The Value1 through Value12 parameters are different for each type of hole. The possible values are as follows, organized by hole type. SOLIDWORKS ignores parameters set to -1.

Value1 through Value12 for different types of holes:

#### Counterbore Holes

Head clearance - Added to either the input counterbore depth or the counterbore depth in the standard.

> Parameters for all counterbore holes:
>
> 1. CounterBore Diameter
> 2. CounterBore Depth
> 3. HeadClearance
> 4. Screw Fit
> 5. Drill Angle
> 6. Near Csink Diameter
> 7. Near Csink Angle
> 8. Bot Csink Diameter
> 9. Bot Csink Angle
> 10. Far Csink Diameter
> 11. Far Csink Angle
> 12. Offset

#### Countersink Holes

Head clearance type - Value from [swWzdHoleCounterSinkHeadClearanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCounterSinkHeadClearanceTypes_e.html), which represents how to add the head clearance values to the hole.

> Parameters for all countersink holes:
>
> 1. Near Csink Diameter
> 2. Near Csink Angle
> 3. Head Clearance
> 4. Screw Fit
> 5. Drill Angle
> 6. Far Csink Diameter
> 7. Far Csink Angle
> 8. Offset
> 9. Head Clearance Type

#### Regular Holes

Parameters for all holes:

1. Screw Fit
2. Drill Angle
3. Near Csink Diameter
4. Near Csink Angle
5. Far Csink Diameter
6. Far Csink Angle
7. Offset

#### Pipe Tapped Holes

Tap Drill Depth - Depth can be set up as a ratio from the standard thread depth or the input thread depth. If the user does specify a tap drill depth, then the calculation from the thread depth is replaced with the specified depth.

Cosmetic Thread Type - Defaults to swCosmeticThreadNone from [swWzdHoleCosmeticThreadTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCosmeticThreadTypes_e.html).

Near countersink angle - Can be calculated from standard data as a default.

Parameters for all ptap holes:

1. Thread Depth
2. Near Csink Diameter
3. Near Csink Angle
4. Far Csink Diameter
5. Far Csink Angle
6. Drill Angle
7. Cosmetic Thread Type
8. Offset

#### Tap Holes

Tap Drill Depth - If the user specifies a tap drill depth, then SOLIDWORKS always uses this depth. Tap drill depths can be calculated:

1. For helicoil holes: Tap drill depth is calculated based on a constant \* tap drill diameter + allowance for tap type (bottoming or plug).
2. For tapped holes: Tap drill depth is calculated from the thread length + advance + allowance for tap type (bottoming or plug).

Thread Depth - If the user specifies thread depth, then SOLIDWORKS always uses this depth. Tap drill depths can be calculated:

1. For helicoil holes: Thread depth is calculated based on a constant (determined by hole type i.e. Insert = 1.0 \* Dia) + thread depth from the standard \* thread major diameter.
2. For tapped holes: based on 2 \* thread diameter.

Cosmetic Thread Type - Specified as defined in swWzdHoleCosmeticThreadTypes\_e.

Hcoil Tap Type - Defaults to swTapTypePlug as defined in [swWzdHoleHcoilTapTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleHcoilTapTypes_e.html); used only for the helicoil standard holes.

Thread end condition - Defaults to swEndThreadTypeBLIND as defined in [swWzdHoleThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleThreadEndCondition_e.html).

Parameters for all ptap holes:

1. Tap drill diameter
2. Tap drill depth
3. Thread Depth
4. Near Csink Diameter
5. Near Csink Angle
6. Far Csink Diameter
7. Far Csink Angle
8. Drill Angle
9. Cosmetic Thread Type
10. Thread End Condition
11. Helicoil Tap Type
12. Offset

#### Legacy Holes

For legacy types of holes StandardIndex, FastenerTypeIndex, and SSize are not relevant, and SOLIDWORKS ignores them.

The sequence of parameters 6 to 19 for different types of legacy holes is as follows:

Simple

1. Diameter
2. Depth
3. Sketch ID

Tapered

1. Minor Diameter
2. Depth
3. Sketch ID
4. Major Diameter

Counterbored

1. Diameter
2. Depth
3. Sketch ID
4. C-Bore Diameter
5. C-Bore Depth

Countersunk

1. Diameter
2. Depth
3. Sketch ID
4. C-Sink Angle
5. C-Sink Diameter

Counterdrilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Drill Diameter
5. C-Drill Depth
6. C-Drill Angle

Simple Drilled

1. Diameter
2. Depth
3. Sketch ID
4. Drill Angle

Tapered Drilled

1. Minor Diameter
2. Depth
3. Sketch ID
4. Major Diameter
5. Drill Angle

C-Bored Drilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Bore Diameter
5. C-Bore Depth
6. Drill Angle

C-Sunk Drilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Sink Diameter
5. C-Sink Angle
6. Drill Angle

C-Drilled Drilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Drill Diameter
5. C-Drill Depth
6. Drill Angle
7. C-Drill Angle

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)
