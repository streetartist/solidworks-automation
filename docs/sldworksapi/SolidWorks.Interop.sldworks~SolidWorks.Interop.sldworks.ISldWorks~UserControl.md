# UserControl Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl`

Gets and sets whether the user has control over the application.
Gets and sets whether the user has control over the application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UserControl As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.UserControl = value
 
value = instance.UserControl
```

```

System.bool UserControl {get; set;}
```

```

property System.bool UserControl {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the user has control over the application, false if not (see **Remarks**)

Remarks

If the SOLIDWORKS application is started by your program, then the SOLIDWORKS application closes when your program ends. However, if you pass control of the SOLIDWORKS application to the end-user, then it remains running after your program ends.

Setting this property to true causes the SOLIDWORKS application to run in the foreground and be visible. Use [ISldWorks::UserControlBackground](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground.md) if you want to run the SOLIDWORKS application in the background and not be visible.

Example

[Run or Attach to SOLIDWORKS (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)  
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)  
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.md)  
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md)  
[IFrame::KeepInvisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.md)
