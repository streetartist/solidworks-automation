# ICreateFeatureMgrView2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateFeatureMgrView2`

Obsolete. Superseded by IModelDoc2::ICreateFeatureMgrView2.
Obsolete. Superseded by [IModelDoc2::ICreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateFeatureMgrView2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateFeatureMgrView2( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String _
) As FeatMgrView
```

```

Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim value As FeatMgrView
 
value = instance.ICreateFeatureMgrView2(Bitmap, ToolTip)
```

```

FeatMgrView ICreateFeatureMgrView2( 
   ref System.int Bitmap,
   System.string ToolTip
)
```

```

FeatMgrView^ ICreateFeatureMgrView2( 
   System.int% Bitmap,
   System.String^ ToolTip
) 
```

#### Parameters

*Bitmap*

*ToolTip*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
