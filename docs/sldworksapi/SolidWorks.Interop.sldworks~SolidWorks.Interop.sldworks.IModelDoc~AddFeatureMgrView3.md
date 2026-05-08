# AddFeatureMgrView3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddFeatureMgrView3`

Obsolete. Superseded by IModelDoc2::AddFeatureMgrView3.
Obsolete. Superseded by [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFeatureMgrView3( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As System.Boolean
 
value = instance.AddFeatureMgrView3(Bitmap, AppView, ToolTip, WhichPane)
```

```

System.bool AddFeatureMgrView3( 
   ref System.int Bitmap,
   ref System.int AppView,
   System.string ToolTip,
   System.int WhichPane
)
```

```

System.bool AddFeatureMgrView3( 
   System.int% Bitmap,
   System.int% AppView,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*Bitmap*

*AppView*

*ToolTip*

*WhichPane*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
