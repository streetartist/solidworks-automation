# CreateFeatureMgrView2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateFeatureMgrView2`

Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2.
Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrView2( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim value As System.Object
 
value = instance.CreateFeatureMgrView2(Bitmap, ToolTip)
```

```

System.object CreateFeatureMgrView2( 
   ref System.int Bitmap,
   System.string ToolTip
)
```

```

System.Object^ CreateFeatureMgrView2( 
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

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
