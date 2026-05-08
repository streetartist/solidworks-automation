# UserControlBackground Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground`

Gets and sets whether the user has control over the application.
Gets and sets whether the user has control over the application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UserControlBackground As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.UserControlBackground = value
 
value = instance.UserControlBackground
```

```

System.bool UserControlBackground {get; set;}
```

```

property System.bool UserControlBackground {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the user has control over the application, false if not (see Remarks)

Remarks

Setting this property to true causes the SOLIDWORKS application to run in the background and not be visible. Use [ISldWorks::UserControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md) if you want to run the SOLIDWORKS application in the foreground and be visible.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md)  
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md)  
[IFrame::KeepInvisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.md)
