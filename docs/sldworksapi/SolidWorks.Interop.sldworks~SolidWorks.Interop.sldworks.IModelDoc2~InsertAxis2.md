# InsertAxis2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertAxis2`

Inserts a reference axis based on the currently selected items with an option to automatically size the axis.
Inserts a reference axis based on the currently selected items with an option to automatically size the axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertAxis2( _
   ByVal AutoSize As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim AutoSize As System.Boolean
Dim value As System.Boolean
 
value = instance.InsertAxis2(AutoSize)
```

```

System.bool InsertAxis2( 
   System.bool AutoSize
)
```

```

System.bool InsertAxis2( 
   System.bool AutoSize
) 
```

#### Parameters

*AutoSize*
:   True if axis is to be automatically sized, false if not

#### Return Value

True if the reference axis is created successfully, false if not

Example

[Create Revolve Features (VBA)](Create_Revolve_Features_Example_VB.htm)  
[Create Revolve Features (VB.NET)](Create_Revolve_Features_Example_VBNET.htm)  
[Create Revolve Features (C#)](Create_Revolve_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
