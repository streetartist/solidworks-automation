# ICreateFeatureMgrView Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateFeatureMgrView`

Obsolete. Superseded by IModelDoc2::ICreateFeatureMgrView.
Obsolete. Superseded by [IModelDoc2::ICreateFeatureMgrView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateFeatureMgrView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateFeatureMgrView( _
   ByRef Bitmap As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim value As FeatMgrView
 
value = instance.ICreateFeatureMgrView(Bitmap)
```

```

FeatMgrView ICreateFeatureMgrView( 
   ref System.int Bitmap
)
```

```

FeatMgrView^ ICreateFeatureMgrView( 
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
