# IsActive Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsActive`

Gets whether the specified assembly component is shown or hidden in this model document.
Gets whether the specified assembly component is shown or hidden in this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsActive( _
   ByVal CompStr As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim CompStr As System.String
Dim value As System.Boolean
 
value = instance.IsActive(CompStr)
```

```

System.bool IsActive( 
   System.string CompStr
)
```

```

System.bool IsActive( 
   System.String^ CompStr
) 
```

#### Parameters

*CompStr*
:   Name specification of the component

#### Return Value

True if component is shown, false if component is hidden

Remarks

The CompStr parameter is the full assembly component name designation. The format of the name designation is:

   parentModel/childModel

where:

childModel is the model whose display status you want to determine. For example, if you want to determine the display status of a part named SPOKE.SLDPRT and if this part is a child of WHEEL.SLDPRT, which itself is a child of AXIS.SLDPRT, then you would specify CompStr as follows:

AXIS/WHEEL/SPOKE

TIP: The assembly component name designation is shown in the lower-left corner of the SOLIDWORKS application when an assembly component is selected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ShowComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowComponent2.md)  
[IModelDoc2::HideComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideComponent2.md)
