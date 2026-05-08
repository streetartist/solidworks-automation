# ICreateFeatureMgrView3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateFeatureMgrView3`

Obsolete. Superseded by IModelDoc2::ICreateFeatureMgrView3.
Obsolete. Superseded by [IModelDoc2::ICreateFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateFeatureMgrView3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateFeatureMgrView3( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.ICreateFeatureMgrView3(Bitmap, ToolTip, WhichPane)
```

```

FeatMgrView ICreateFeatureMgrView3( 
   ref System.int Bitmap,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ ICreateFeatureMgrView3( 
   System.int% Bitmap,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*Bitmap*

*ToolTip*

*WhichPane*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
