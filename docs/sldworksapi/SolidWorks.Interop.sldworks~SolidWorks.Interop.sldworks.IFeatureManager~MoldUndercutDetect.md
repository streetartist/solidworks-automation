# MoldUndercutDetect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoldUndercutDetect`

Obsolete. Superseded by IFeatureManager::MoldUndercutDetect2.
Obsolete. Superseded by [IFeatureManager::MoldUndercutDetect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoldUndercutDetect2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub MoldUndercutDetect( _
   ByVal ColUndercut As System.Integer, _
   ByVal ColBase As System.Integer, _
   ByVal BCoordInput As System.Boolean, _
   ByVal Dx As System.Double, _
   ByVal Dy As System.Double, _
   ByVal Dz As System.Double _
) 
```

```

Dim instance As IFeatureManager
Dim ColUndercut As System.Integer
Dim ColBase As System.Integer
Dim BCoordInput As System.Boolean
Dim Dx As System.Double
Dim Dy As System.Double
Dim Dz As System.Double
 
instance.MoldUndercutDetect(ColUndercut, ColBase, BCoordInput, Dx, Dy, Dz)
```

```

void MoldUndercutDetect( 
   System.int ColUndercut,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
)
```

```

void MoldUndercutDetect( 
   System.int ColUndercut,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
) 
```

#### Parameters

*ColUndercut*

*ColBase*

*BCoordInput*

*Dx*

*Dy*

*Dz*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
