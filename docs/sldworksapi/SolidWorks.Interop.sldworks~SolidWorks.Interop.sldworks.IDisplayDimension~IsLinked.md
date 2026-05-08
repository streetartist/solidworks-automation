# IsLinked Property (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked`

Gets whether the dimension has text linked to it.
Gets whether the dimension has text linked to it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsLinked As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.IsLinked
```

```

System.bool IsLinked {get;}
```

```

property System.bool IsLinked {
   System.bool get();
}
```

#### Property Value

True if the text is linked to the dimension, false if not

Example

[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.md)  
[IDisplayDimension::SetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText.md)  
[IDisplayDimension::Unlink Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink.md)
