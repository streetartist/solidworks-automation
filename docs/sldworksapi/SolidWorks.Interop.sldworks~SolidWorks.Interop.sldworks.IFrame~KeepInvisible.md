# KeepInvisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible`

Gets or sets whether to keep the SOLIDWORKS frame invisible.
Gets or sets whether to keep the SOLIDWORKS frame invisible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepInvisible As System.Boolean
```

```

Dim instance As IFrame
Dim value As System.Boolean
 
instance.KeepInvisible = value
 
value = instance.KeepInvisible
```

```

System.bool KeepInvisible {get; set;}
```

```

property System.bool KeepInvisible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep the SOLIDWORKS frame invisible, false to keep it visible

Remarks

Use this property when SOLIDWORKS is [invisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md) and you want to [activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.md) a component and prevent SOLIDWORKS from becoming visible. Be sure to set this property back to false after the operation for which you set it to true completes.

Example

[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md)  
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md)  
[ISldWorks::UserControlBackground Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground.md)
