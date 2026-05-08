# MoldUndercutDetect2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoldUndercutDetect2`

Detects trapped, also called undercut, areas in a model that cannot be ejected from the mold.
Detects trapped, also called undercut, areas in a model that cannot be ejected from the mold.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub MoldUndercutDetect2( _
   ByVal ColUndercut1 As System.Integer, _
   ByVal ColUndercut2 As System.Integer, _
   ByVal ColOccluded As System.Integer, _
   ByVal ColStraddle As System.Integer, _
   ByVal ColBase As System.Integer, _
   ByVal BCoordInput As System.Boolean, _
   ByVal Dx As System.Double, _
   ByVal Dy As System.Double, _
   ByVal Dz As System.Double _
) 
```

```

Dim instance As IFeatureManager
Dim ColUndercut1 As System.Integer
Dim ColUndercut2 As System.Integer
Dim ColOccluded As System.Integer
Dim ColStraddle As System.Integer
Dim ColBase As System.Integer
Dim BCoordInput As System.Boolean
Dim Dx As System.Double
Dim Dy As System.Double
Dim Dz As System.Double
 
instance.MoldUndercutDetect2(ColUndercut1, ColUndercut2, ColOccluded, ColStraddle, ColBase, BCoordInput, Dx, Dy, Dz)
```

```

void MoldUndercutDetect2( 
   System.int ColUndercut1,
   System.int ColUndercut2,
   System.int ColOccluded,
   System.int ColStraddle,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
)
```

```

void MoldUndercutDetect2( 
   System.int ColUndercut1,
   System.int ColUndercut2,
   System.int ColOccluded,
   System.int ColStraddle,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
) 
```

#### Parameters

*ColUndercut1*
:   Value (COLORREF type) that specifies the color for the faces invisible from one direction that form an undercut

*ColUndercut2*
:   Value (COLORREF type) that specifies the color for the faces invisible from a second direction that form an undercut

*ColOccluded*
:   Value (COLORREF type) that specifies the color for the faces invisible from both directions that form an undercut

*ColStraddle*
:   Value (COLORREF type) that specifies the color for the faces with draft in both directions that form an undercut

*ColBase*
:   Value (COLORREF type) that specifies the color for the faces that do not form undercuts; that is, all faces except the undercut faces

*BCoordInput*
:   True to enable coordinate input to control the direction of pull, false to not

*Dx*
:   x coordinate to control the direction of pull

*Dy*
:   y coordinate to control the direction of pull

*Dz*
:   z coordinate to control the direction of pull

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)
