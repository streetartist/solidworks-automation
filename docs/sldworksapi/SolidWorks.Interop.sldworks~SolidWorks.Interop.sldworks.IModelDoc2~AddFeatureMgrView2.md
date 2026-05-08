# AddFeatureMgrView2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView2`

Obsolete. Superseded by IModelDoc2::AddFeatureMgrView3.
Obsolete. Superseded by [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFeatureMgrView2( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim ToolTip As System.String
Dim value As System.Boolean
 
value = instance.AddFeatureMgrView2(Bitmap, AppView, ToolTip)
```

```

System.bool AddFeatureMgrView2( 
   ref System.int Bitmap,
   ref System.int AppView,
   System.string ToolTip
)
```

```

System.bool AddFeatureMgrView2( 
   System.int% Bitmap,
   System.int% AppView,
   System.String^ ToolTip
) 
```

#### Parameters

*Bitmap*

*AppView*

*ToolTip*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
