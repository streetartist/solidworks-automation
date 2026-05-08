# InsertCrossBreak Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCrossBreak`

Inserts a cross break feature on the selected face in a sheet metal part.
Inserts a cross break feature on the selected face in a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCrossBreak( _
   ByVal Angle As System.Double, _
   ByVal Radius As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angle As System.Double
Dim Radius As System.Double
Dim value As Feature
 
value = instance.InsertCrossBreak(Angle, Radius)
```

```

Feature InsertCrossBreak( 
   System.double Angle,
   System.double Radius
)
```

```

Feature^ InsertCrossBreak( 
   System.double Angle,
   System.double Radius
) 
```

#### Parameters

*Angle*
:   Break angle

*Radius*
:   Break radius

#### Return Value

Cross break [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)  
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)  
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.md)
