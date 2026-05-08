# Visible Property (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible`

Gets and sets the visibility property of the SOLIDWORKS application.
Gets and sets the visibility property of the SOLIDWORKS application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.Visible = value
 
value = instance.Visible
```

```

System.bool Visible {get; set;}
```

```

property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the application is visible, false if not

Remarks

If the SOLIDWORKS application is started by your program, then the SOLIDWORKS application closes when your program ends. It makes no difference whether you make the SOLIDWORKS session visible.

However, if your program started the SOLIDWORKS application and you assign control of the SOLIDWORKS application to the end-user using [ISldWorks::UserControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md), then it remains running even when your program ends.

Also, the SOLIDWORKS application can only be hidden if ISldWorks::UserControl is false and there are no visible documents open.

Example

[Open Document (VBA)](Open_Document_Example_VB.htm)  
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
[IFrame::KeepInvisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.md)  
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md)  
[ISldWorks::UserControlBackground Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground.md)
