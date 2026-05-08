# InsertSheetMetalBaseFlange Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalBaseFlange`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalBaseFlange.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalBaseFlange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSheetMetalBaseFlange( _
   ByVal Thickness As System.Double, _
   ByVal ThickenDir As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal ExtrudeDist1 As System.Double, _
   ByVal ExtrudeDist2 As System.Double, _
   ByVal FlipExtruDir As System.Boolean, _
   ByVal EndCondition1 As System.Integer, _
   ByVal EndCondition2 As System.Integer, _
   ByVal DirToUse As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim ThickenDir As System.Boolean
Dim Radius As System.Double
Dim ExtrudeDist1 As System.Double
Dim ExtrudeDist2 As System.Double
Dim FlipExtruDir As System.Boolean
Dim EndCondition1 As System.Integer
Dim EndCondition2 As System.Integer
Dim DirToUse As System.Integer
 
instance.InsertSheetMetalBaseFlange(Thickness, ThickenDir, Radius, ExtrudeDist1, ExtrudeDist2, FlipExtruDir, EndCondition1, EndCondition2, DirToUse)
```

```

void InsertSheetMetalBaseFlange( 
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse
)
```

```

void InsertSheetMetalBaseFlange( 
   System.double Thickness,
   System.bool ThickenDir,
   System.double Radius,
   System.double ExtrudeDist1,
   System.double ExtrudeDist2,
   System.bool FlipExtruDir,
   System.int EndCondition1,
   System.int EndCondition2,
   System.int DirToUse
) 
```

#### Parameters

*Thickness*

*ThickenDir*

*Radius*

*ExtrudeDist1*

*ExtrudeDist2*

*FlipExtruDir*

*EndCondition1*

*EndCondition2*

*DirToUse*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
