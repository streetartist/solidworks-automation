# CopyAppearance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyAppearance`

Copies the appearance of the specified entity to the clipboard.
Copies the appearance of the specified entity to the clipboard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CopyAppearance( _
   ByVal Object As System.Object _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Object As System.Object
Dim value As System.Boolean
 
value = instance.CopyAppearance(Object)
```

```

System.bool CopyAppearance( 
   System.object Object
)
```

```

System.bool CopyAppearance( 
   System.Object^ Object
) 
```

#### Parameters

*Object*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md), or [part](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) whose appearance you want to copy

#### Return Value

True if appearance is successfully copied to the clipboard, false if not

Example

[Copy and Paste Appearances (VBA)](Copy_and_Paste_Appearances_Example_VB.htm)  
[Copy and Paste Appearances (VB.NET)](Copy_and_Paste_Appearances_Example_VBNET.htm)  
[Copy and Paste Appearances (C#)](Copy_and_Paste_Appearances_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::PasteAppearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PasteAppearance.md)
