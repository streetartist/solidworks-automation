# InsertCosmeticThread Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread`

Obsolete. Superseded by IFeatureManager::InsertCosmeticThread2.
Obsolete. Superseded by [IFeatureManager::InsertCosmeticThread2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCosmeticThread( _
   ByVal Type As System.Short, _
   ByVal Depth As System.Double, _
   ByVal Length As System.Double, _
   ByVal Note As System.String _
) As System.String
```

```

Dim instance As IFeatureManager
Dim Type As System.Short
Dim Depth As System.Double
Dim Length As System.Double
Dim Note As System.String
Dim value As System.String
 
value = instance.InsertCosmeticThread(Type, Depth, Length, Note)
```

```

System.string InsertCosmeticThread( 
   System.short Type,
   System.double Depth,
   System.double Length,
   System.string Note
)
```

```

System.String^ InsertCosmeticThread( 
   System.short Type,
   System.double Depth,
   System.double Length,
   System.String^ Note
) 
```

#### Parameters

*Type*

*Depth*

*Length*

*Note*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
