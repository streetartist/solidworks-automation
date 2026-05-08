# IsTessellationValid Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsTessellationValid`

Gets whether the current set of facets is valid.
Gets whether the current set of facets is valid.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTessellationValid() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.IsTessellationValid()
```

```

System.bool IsTessellationValid()
```

```

System.bool IsTessellationValid(); 
```

#### Return Value

True if the facet data is valid; false if not

Remarks

This method captures operations that invalidate the current set of facets, but does not send a RegenNotify event. For example, if the user changes the rendering tolerance, the RegenNotify event is not sent. However, the current set of facets would be invalid. This action triggers a RepaintNotify from which you can call this method before attempting to use your current set of facet data.

If false is returned, then valid facet information would not be available until SOLIDWORKS completes a repaint operation (RepaintPostNotify). In other words, SOLIDWORKS does not have any valid facet information at this time, and any facet data obtained in earlier calls is invalid.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)
