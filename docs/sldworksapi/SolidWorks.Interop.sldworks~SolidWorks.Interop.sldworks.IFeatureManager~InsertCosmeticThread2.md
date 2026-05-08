# InsertCosmeticThread2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread2`

Obsolete. Superseded by IFeatureManager::InsertCosmeticThread3.
Obsolete. Superseded by [IFeatureManager::InsertCosmeticThread3.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread3.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCosmeticThread2( _
   ByVal Type As System.Short, _
   ByVal Depth As System.Double, _
   ByVal Length As System.Double, _
   ByVal Note As System.String _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type As System.Short
Dim Depth As System.Double
Dim Length As System.Double
Dim Note As System.String
Dim value As Feature
 
value = instance.InsertCosmeticThread2(Type, Depth, Length, Note)
```

```

Feature InsertCosmeticThread2( 
   System.short Type,
   System.double Depth,
   System.double Length,
   System.string Note
)
```

```

Feature^ InsertCosmeticThread2( 
   System.short Type,
   System.double Depth,
   System.double Length,
   System.String^ Note
) 
```

#### Parameters

*Type*
:   Type as defined in [swCosmeticThreadType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticThreadType_e.html)

*Depth*
:   Diameter of the cosmetic thread

*Length*
:   Length of the cosmetic thread

*Note*
:   Callout text to display in the drawing document

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)
