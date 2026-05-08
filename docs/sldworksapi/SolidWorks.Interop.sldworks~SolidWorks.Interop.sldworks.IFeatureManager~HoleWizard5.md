# HoleWizard5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard5`

Creates customized holes of various kinds.
Creates customized holes of various kinds.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HoleWizard5( _
   ByVal GenericHoleType As System.Integer, _
   ByVal StandardIndex As System.Integer, _
   ByVal FastenerTypeIndex As System.Integer, _
   ByVal SSize As System.String, _
   ByVal EndType As System.Short, _
   ByVal Diameter As System.Double, _
   ByVal Depth As System.Double, _
   ByVal Length As System.Double, _
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
   ByVal FeatureScope As System.Boolean, _
   ByVal AutoSelect As System.Boolean, _
   ByVal AssemblyFeatureScope As System.Boolean, _
   ByVal AutoSelectComponents As System.Boolean, _
   ByVal PropagateFeatureToParts As System.Boolean _
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
Dim Length As System.Double
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
Dim FeatureScope As System.Boolean
Dim AutoSelect As System.Boolean
Dim AssemblyFeatureScope As System.Boolean
Dim AutoSelectComponents As System.Boolean
Dim PropagateFeatureToParts As System.Boolean
Dim value As Feature
 
value = instance.HoleWizard5(GenericHoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, Diameter, Depth, Length, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9, Value10, Value11, Value12, ThreadClass, RevDir, FeatureScope, AutoSelect, AssemblyFeatureScope, AutoSelectComponents, PropagateFeatureToParts)
```

```

Feature HoleWizard5( 
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.string SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Length,
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
   System.bool FeatureScope,
   System.bool AutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts
)
```

```

Feature^ HoleWizard5( 
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.String^ SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Length,
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
   System.bool FeatureScope,
   System.bool AutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents,
   System.bool PropagateFeatureToParts
) 
```

#### Parameters

*GenericHoleType*
:   Type of hole or slot as defined in [swWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdGeneralHoleTypes_e.html)

*StandardIndex*
:   Hole or slot standard property as defined in [swWzdHoleStandards\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html) (see **Remarks** for legacy holes)

*FastenerTypeIndex*
:   Hole or slot fastener type as defined in [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html) (see **Remarks**)

*SSize*
:   Size of the hole or slot (see **Remarks**)

*EndType*
:   Hole or slot end type as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html) (see **Remarks**)

*Diameter*
:   Diameter of the hole or slot

*Depth*
:   Depth of the hole or slot

*Length*
:   Length of slot; valid only if GenericHoleType set to:

    - swWzdGeneralHoleTypes\_e.swWzdCounterBoreSlot
    - swWzdGeneralHoleTypes\_e.swWzdCounterSinkSlot
    - swWzdGeneralHoleTypes\_e.swWzdHoleSlot

    For both straight/pipe and tapered tap holes, the macro recorder fails to properly record this parameter. Before running a macro recording, you must add -1 at this position and delete a -1 before ThreadClass.

*Value1*
:   Hole or slot parameter

*Value2*
:   Hole or slot parameter

*Value3*
:   Hole or slot parameter

*Value4*
:   Hole or slot parameter

*Value5*
:   Hole or slot parameter

*Value6*
:   Hole or slot parameter

*Value7*
:   Hole or slot parameter

*Value8*
:   Hole or slot parameter

*Value9*
:   Hole or slot parameter

*Value10*
:   Hole or slot parameter

*Value11*
:   Hole or slot parameter

*Value12*
:   Hole or slot parameter

*ThreadClass*
:   One of the following thread classes:

    - 1B
    - 2B
    - 3B

    **NOTE**: Applies to ANSI inch standard only.

*RevDir*
:   True to reverse the direction of the hole or slot, false to not

*FeatureScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*AutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects

*AssemblyFeatureScope*
:   True if the assembly feature only affects selected components in the assembly, false if the assembly feature affects all components in the assembly

*AutoSelectComponents*
:   True to automatically select all affected components, false to only use the selected components

*PropagateFeatureToParts*
:   True to propagate the assembly feature to the components that the assembly feature affects in the model, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

To create simple holes and slots, read [Hole Wizard Features and WizardHoleFeatureData2 Objects](sldworksapiprogguide.chm::/OVERVIEW/Hole_Wizard_Features_and_WizardHoleFeatureData2_Objects.htm). To create Advanced Holes of stacked hole elements, use [IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.md).

Valid types of slots are counterbore, countersink, or straight.

To add a hole or slot at one or more locations, call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) with Mark = 0 for each location.

Before creating a hole or slot using a reference plane and this method, determine the value of the RevDir parameter as follows:

- If the material is on one side of the reference plane, then RevDir is false.
- If the material is on both sides of the reference plane, then compare the distances between the reference plane and the material on both sides. If the distance between the reference plane and the material along its normal direction is bigger, then RevDir is true; otherwise, RevDir is false.

You can also use [IModelDoc2::RayIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.md) and [IModelDoc2::GetRayIntersectionsPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.md) to find out if the material is on one side or both sides and to compare the distances.

**Parameters for this method:**

- The FastenerTypeIndex parameter has to match the standard and be valid for that hole or slot type, or an error occurs.
- The SSize parameter must be a valid size for the fastener type, or an error occurs.
- If EndType is 10 = swEndCondUpToSelection (supersedes swEndCondUpToSurface and swEndCondUpToVertex), then you must use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 2 to pre-select the surface or vertex. The macro recorder fails to properly record EndType for Up To Surface and Up To Vertex end conditions. Instead of swEndCondUpToSelection=10, it records 4 and 3. Before running an Up to Surface or Vertex macro recording, you must change EndType to 10. The macro recorder also fails to properly record the Up To Next end condition. Instead of swEndCondUpToNext=11, it records swEndCondThroughNext=2. It is advisable to record only Blind or Through All end conditions.
- Screw fit is defined as [swWzdHoleScrewClearanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleScrewClearanceTypes_e.html) and is only used if a hole or slot diameter is not specified; default value is NORMAL\_FIT.
- Drill angle defaults to 118 degrees (2.05948851735331 radians), if not specified.
- Input angles are in radians; input values are in meters.
- The Value1 through Value12 parameters are different for each type of hole or slot. The possible values are as follows, organized by hole and slot type. SOLIDWORKS ignores parameters set to -1.

> #### Counterbore Holes and Slots
>
> Head Clearance - Added to either the input counterbore depth or the counterbore depth in the standard.
>
> **Screw Fit** - Value from swWzdHoleScrewClearanceTypes\_e
>
> Parameters for all counterbore holes and counterbore slots:
>
> 1. CounterBore Diameter
> 2. CounterBore Depth
> 3. Head Clearance
> 4. Screw Fit
> 5. Drill Angle at Bottom (valid only if EndType is \*not\* swEndCondUpToNext or swEndCondThroughAll)
> 6. Near Csink Diameter
> 7. Near Csink Angle
> 8. Underhead Csink Diameter
> 9. Underhead Csink Angle
> 10. Far Csink Diameter
> 11. Far Csink Angle
> 12. Offset (valid only if EndType is swEndCondOffsetFromSurface)
>
> #### Countersink Holes and Slots
>
> Head Clearance Type - Value from [swWzdHoleCounterSinkHeadClearanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCounterSinkHeadClearanceTypes_e.html), which represents how to add the head clearance values to the hole or slot.
>
> **Screw Fit** - Value from **swWzdHoleScrewClearanceTypes\_e**
>
> Parameters for all countersink holes and countersink slots:
>
> 1. Near Csink Diameter
> 2. Near Csink Angle
> 3. Head Clearance
> 4. Screw Fit
> 5. Drill Angle at Bottom (valid only if EndType is \*not\* swEndCondUpToNext or swEndCondThroughAll)
> 6. Far Csink Diameter
> 7. Far Csink Angle
> 8. Offset (valid only if EndType is swEndCondOffsetFromSurface)
> 9. Head Clearance Type
> 10. -1
> 11. -1
> 12. -1
>
> #### Regular Holes and Straight Slots
>
> **Screw Fit** - Value from **swWzdHoleScrewClearanceTypes\_e**
>
> Parameters for all regular holes and straight slots:
>
> 1. Screw Fit
> 2. Drill Angle at Bottom (valid only if EndType is \*not\* swEndCondUpToNext or swEndCondThroughAll)
> 3. Near Csink Diameter
> 4. Near Csink Angle
> 5. Far Csink Diameter
> 6. Far Csink Angle
> 7. Offset (valid only if EndType is swEndCondOffsetFromSurface)
> 8. -1
> 9. -1
> 10. -1
> 11. -1
> 12. -1
>
> #### Pipe/Straight Tap Holes
>
> Tap Thread Depth - If the user specifies thread depth, SOLIDWORKS always uses this depth. Tap thread depths can be calculated:
>
> - Helicoil holes: calculated based on a constant (determined by hole type; i.e., insert = 1.0 \* diameter) + thread depth from the standard \* thread major diameter.
> - Tapped holes: calculated based on 2 \* thread diameter.
>
> Cosmetic Thread Type - Value from [swWzdHoleCosmeticThreadTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCosmeticThreadTypes_e.html); defaults to swCosmeticThreadNone
>
> Near Countersink Angle - Can be calculated from standard data as a default
>
> Hcoil Tap Type - Value from [swWzdHoleHcoilTapTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleHcoilTapTypes_e.html); defaults to swTapTypePlug
>
> Thread End Condition - Value from [swWzdHoleThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleThreadEndCondition_e.html); defaults to swEndThreadTypeBLIND
>
> Parameters for all pipe/straight tap holes:
>
> 1. Tap Thread Depth
> 2. Near Csink Diameter
> 3. Near Csink Angle
> 4. Far Csink Diameter
> 5. Far Csink Angle
> 6. Drill Angle at Bottom (valid only if EndType is \*not\* swEndCondUpToNext or swEndCondThroughAll)
> 7. Cosmetic Thread Type
> 8. Thread End Condition (not valid if StandardIndex is swStandardHelicoilInch or swStandardHelicoilMetric)
> 9. Helicoil Tap Type (valid only if StandardIndex is swStandardHelicoilInch or swStandardHelicoilMetric)
> 10. Offset (valid only if EndType is swEndCondOffsetFromSurface)
> 11. -1
> 12. -1
>
> #### Tapered Tap Holes
>
> NOTE: The macro recorder fails to properly record tapered tap hole parameters. Follow the instructions in this help to correct recordings before playing them.
>
> Cosmetic Thread Type - Specified as defined in swWzdHoleCosmeticThreadTypes\_e; defaults to swCosmeticThreadNone
>
> Parameters for all tapered tap holes:
>
> 1. Tap Thread Depth
> 2. Near Csink Diameter
> 3. Near Csink Angle
> 4. Far Csink Diameter
> 5. Far Csink Angle
> 6. Drill Angle at Bottom (valid only if EndType is \*not\* swEndCondUpToNext or swEndCondThroughAll)
> 7. Cosmetic Thread Type
> 8. Offset (valid only if EndType is swEndCondOffsetFromSurface)
> 9. -1
> 10. -1
> 11. -1
> 12. -1
>
> #### Legacy Holes
>
> StandardIndex, FastenerTypeIndex, and SSize are:
>
> - Not relevant
> - SOLIDWORKS ignores them
>
> Value1 - Value12 for different types of legacy holes. Use -1 for unused values:
>
> Simple
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
>
> Tapered
>
> 1. Minor Diameter
> 2. Depth
> 3. Sketch ID
> 4. Major Diameter
>
> Counterbored
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. C-Bore Diameter
> 5. C-Bore Depth
>
> Countersunk
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. C-Sink Angle
> 5. C-Sink Diameter
>
> Counterdrilled
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. C-Drill Diameter
> 5. C-Drill Depth
> 6. C-Drill Angle
>
> Simple Drilled
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. Drill Angle
>
> Tapered Drilled
>
> 1. Minor Diameter
> 2. Depth
> 3. Sketch ID
> 4. Major Diameter
> 5. Drill Angle
>
> C-Bored Drilled
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. C-Bore Diameter
> 5. C-Bore Depth
> 6. Drill Angle
>
> C-Sunk Drilled
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. C-Sink Diameter
> 5. C-Sink Angle
> 6. Drill Angle
>
> C-Drilled Drilled
>
> 1. Diameter
> 2. Depth
> 3. Sketch ID
> 4. C-Drill Diameter
> 5. C-Drill Depth
> 6. Drill Angle
> 7. C-Drill Angle

Example

[Create Hole Wizard Hole (C#)](Create_Hole_Wizard_Hole_Example_CSharp.htm)  
[Create Hole Wizard Hole (VB.NET)](Create_Hole_Wizard_Hole_Example_VBNET.htm)  
[Create Hole Wizard Hole (VBA)](Create_Hole_Wizard_Hole_Example_VB.htm)  
[Insert Hole Wizard Slot and Hole (C#)](Insert_Hole_Wizard_Slot_and_Hole_Example_CSharp.htm)  
[Insert Hole Wizard Slot and Hole (VB.NET)](Insert_Hole_Wizard_Slot_and_Hole_Example_VBNET.htm)  
[Insert Hole Wizard Slot and Hole (VBA)](Insert_Hole_Wizard_Slot_and_Hole_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)
