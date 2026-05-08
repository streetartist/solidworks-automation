# CreateFeatureMgrView Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateFeatureMgrView`

Obsolete. Superseded by IModelDoc2::CreateFeatureManager.
Obsolete. Superseded by [IModelDoc2::CreateFeatureManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateFeatureMgrView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrView( _
   ByRef Bitmap As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim value As System.Object
 
value = instance.CreateFeatureMgrView(Bitmap)
```

```

System.object CreateFeatureMgrView( 
   ref System.int Bitmap
)
```

```

System.Object^ CreateFeatureMgrView( 
   System.int% Bitmap
) 
```

#### Parameters

*Bitmap*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
