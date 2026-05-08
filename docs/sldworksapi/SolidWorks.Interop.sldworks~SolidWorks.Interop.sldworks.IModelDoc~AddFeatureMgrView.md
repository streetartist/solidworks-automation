# AddFeatureMgrView Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddFeatureMgrView`

Obsolete. Superseded by IModelDoc2::AddFeatureMgrView.
Obsolete. Superseded by [IModelDoc2::AddFeatureMgrView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFeatureMgrView( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim value As System.Boolean
 
value = instance.AddFeatureMgrView(Bitmap, AppView)
```

```

System.bool AddFeatureMgrView( 
   ref System.int Bitmap,
   ref System.int AppView
)
```

```

System.bool AddFeatureMgrView( 
   System.int% Bitmap,
   System.int% AppView
) 
```

#### Parameters

*Bitmap*

*AppView*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
