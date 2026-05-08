# InsertSheetMetal3dBend Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetal3dBend`

Obsolete. Superseded by IFeatureManager::InsertSheetMetal3dBend.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetal3dBend](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetal3dBend.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSheetMetal3dBend( _
   ByVal Angle As System.Double, _
   ByVal Radius As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal BendPos As System.Short _
) 
```

```

Dim instance As IModelDoc2
Dim Angle As System.Double
Dim Radius As System.Double
Dim FlipDir As System.Boolean
Dim BendPos As System.Short
 
instance.InsertSheetMetal3dBend(Angle, Radius, FlipDir, BendPos)
```

```

void InsertSheetMetal3dBend( 
   System.double Angle,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos
)
```

```

void InsertSheetMetal3dBend( 
   System.double Angle,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos
) 
```

#### Parameters

*Angle*

*Radius*

*FlipDir*

*BendPos*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
