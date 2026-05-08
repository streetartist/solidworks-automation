# SelectComponentsBySize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectComponentsBySize`

Selects assembly components by percent of assembly size.
Selects assembly components by percent of assembly size.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectComponentsBySize( _
   ByVal Percent As System.Double _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Percent As System.Double
Dim value As System.Boolean
 
value = instance.SelectComponentsBySize(Percent)
```

```

System.bool SelectComponentsBySize( 
   System.double Percent
)
```

```

System.bool SelectComponentsBySize( 
   System.double Percent
) 
```

#### Parameters

*Percent*
:   0.0 <= Percent of assembly size <= 100.0

#### Return Value

True if Percent is valid, false if Percent > 100 or Percent < 0

Remarks

This method corresponds to **Tools > Component Selection > Select By Size**.

Example

[Select Assembly Components by Size (VBA)](Select_Assembly_Components_by_Size_Example_VB.htm)  
[Select Assembly Components by Size (VB.NET)](Select_Assembly_Components_by_Size_Example_VBNET.htm)  
[Select Assembly Components by Size (C#)](Select_Assembly_Components_by_Size_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IModelDocExtension::SelectByID2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[IModelDocExtension::SelectAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)
