# InitializeHole Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~InitializeHole`

Initializes a newly created Hole Wizard feature data object.
Initializes a newly created Hole Wizard feature data object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InitializeHole( _
   ByVal GenericHoleType As System.Integer, _
   ByVal StdIndex As System.Integer, _
   ByVal FastnerType As System.Integer, _
   ByVal SSize As System.String, _
   ByVal EndType As System.Integer _
) 
```

```

Dim instance As IWizardHoleFeatureData2
Dim GenericHoleType As System.Integer
Dim StdIndex As System.Integer
Dim FastnerType As System.Integer
Dim SSize As System.String
Dim EndType As System.Integer
 
instance.InitializeHole(GenericHoleType, StdIndex, FastnerType, SSize, EndType)
```

```

void InitializeHole( 
   System.int GenericHoleType,
   System.int StdIndex,
   System.int FastnerType,
   System.string SSize,
   System.int EndType
)
```

```

void InitializeHole( 
   System.int GenericHoleType,
   System.int StdIndex,
   System.int FastnerType,
   System.String^ SSize,
   System.int EndType
) 
```

#### Parameters

*GenericHoleType*
:   Hole type as defined in [swWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdGeneralHoleTypes_e.html)

*StdIndex*
:   Standard as defined in [swWzdHoleStandards\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)

*FastnerType*
:   Screw type as defined in [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

*SSize*
:   Size of the hole

*EndType*
:   End type as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

Remarks

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)
