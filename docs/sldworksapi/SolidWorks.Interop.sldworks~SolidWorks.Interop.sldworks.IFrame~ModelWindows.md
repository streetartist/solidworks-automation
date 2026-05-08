# ModelWindows Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows`

Gets the client model windows for this frame.
Gets the client model windows for this frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ModelWindows As System.Object
```

```

Dim instance As IFrame
Dim value As System.Object
 
value = instance.ModelWindows
```

```

System.object ModelWindows {get;}
```

```

property System.Object^ ModelWindows {
   System.Object^ get();
}
```

#### Property Value

Array of the client [model windows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md) of this frame

Example

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)  
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)  
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)
