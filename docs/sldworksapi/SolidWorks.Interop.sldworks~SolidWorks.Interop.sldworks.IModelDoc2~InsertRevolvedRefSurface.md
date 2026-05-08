# InsertRevolvedRefSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRevolvedRefSurface`

Obsolete. Superseded by IFeatureManager::InsertRevolvedRefSurface.
Obsolete. Superseded by [IFeatureManager::InsertRevolvedRefSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRevolvedRefSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertRevolvedRefSurface( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
 
instance.InsertRevolvedRefSurface(Angle, ReverseDir, Angle2, RevType)
```

```

void InsertRevolvedRefSurface( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

```

void InsertRevolvedRefSurface( 
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
) 
```

#### Parameters

*Angle*

*ReverseDir*

*Angle2*

*RevType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
