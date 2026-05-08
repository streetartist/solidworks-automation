# InsertSheetMetalCornerTrim Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalCornerTrim`

Inserts a break corner trim in the sheet metal part.
Inserts a break corner trim in the sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalCornerTrim( _
   ByVal InternalCornerFlag As System.Integer, _
   ByVal BreakType As System.Integer, _
   ByVal BreakDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal Param As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim InternalCornerFlag As System.Integer
Dim BreakType As System.Integer
Dim BreakDist As System.Double
Dim ReliefType As System.Integer
Dim Param As System.Double
Dim value As Feature
 
value = instance.InsertSheetMetalCornerTrim(InternalCornerFlag, BreakType, BreakDist, ReliefType, Param)
```

```

Feature InsertSheetMetalCornerTrim( 
   System.int InternalCornerFlag,
   System.int BreakType,
   System.double BreakDist,
   System.int ReliefType,
   System.double Param
)
```

```

Feature^ InsertSheetMetalCornerTrim( 
   System.int InternalCornerFlag,
   System.int BreakType,
   System.double BreakDist,
   System.int ReliefType,
   System.double Param
) 
```

#### Parameters

*InternalCornerFlag*
:   Do internal corners only

*BreakType*
:   Type of break as defined in [swBreakCornerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)

*BreakDist*
:   Distance to break from corner

*ReliefType*
:   Type of relief:

    - 0 = circular
    - 1 = square
    - 2 = bend-waist

*Param*
:   ReliefType dependent:

    - circular, its diameter
    - square, its side length
    - bend-waist, its radius

#### Return Value

Pointer to the break corner trim [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) in the sheet metal part

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
