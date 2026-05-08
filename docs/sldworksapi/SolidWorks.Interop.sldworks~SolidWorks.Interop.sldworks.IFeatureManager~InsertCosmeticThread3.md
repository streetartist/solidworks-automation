# InsertCosmeticThread3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread3`

Inserts a cosmetic thread.
Inserts a cosmetic thread.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCosmeticThread3( _
   ByVal Standard As System.Integer, _
   ByVal StandardType As System.String, _
   ByVal Size As System.String, _
   ByVal Diameter As System.Double, _
   ByVal EndType As System.Integer, _
   ByVal Depth As System.Double, _
   ByVal Note As System.String _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Standard As System.Integer
Dim StandardType As System.String
Dim Size As System.String
Dim Diameter As System.Double
Dim EndType As System.Integer
Dim Depth As System.Double
Dim Note As System.String
Dim value As Feature
 
value = instance.InsertCosmeticThread3(Standard, StandardType, Size, Diameter, EndType, Depth, Note)
```

```

Feature InsertCosmeticThread3( 
   System.int Standard,
   System.string StandardType,
   System.string Size,
   System.double Diameter,
   System.int EndType,
   System.double Depth,
   System.string Note
)
```

```

Feature^ InsertCosmeticThread3( 
   System.int Standard,
   System.String^ StandardType,
   System.String^ Size,
   System.double Diameter,
   System.int EndType,
   System.double Depth,
   System.String^ Note
) 
```

#### Parameters

*Standard*
:   Thread standard as defined by [swCosmeticStandardType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticStandardType_e.html)

*StandardType*
:   Thread type for Standard

*Size*
:   Thread size for the specified Standard

*Diameter*
:   Thread diameter

*EndType*
:   End condition as defined by [swCosmeticEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticEndConditions_e.html)

*Depth*
:   Depth of the cosmetic thread; valid only for EndType = swCosmeticEndConditions\_e.swEndConditionBlind or swCosmeticEndConditions\_e.swEndConditionBlindUptoNext or swCosmeticEndConditions\_e.swEndConditionBlind2Dia

*Note*
:   Callout text to display in the drawing document

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)  
[Traverse All Cosmetic Threads (VB.NET)](Traverse_All_Cosmetic_Threads_Example_VBNET.htm)  
[Traverse All Cosmetic Threads (C#)](Traverse_All_Cosmetic_Threads_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)
