# UniqueName Property (IMessageBarDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~UniqueName`

Gets the ID of this message bar.
Gets the ID of this message bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UniqueName As System.String
```

```

Dim instance As IMessageBarDefinition
Dim value As System.String
 
value = instance.UniqueName
```

```

System.string UniqueName {get;}
```

```

property System.String^ UniqueName {
   System.String^ get();
}
```

#### Property Value

Unique ID of this message bar

Remarks

The ID is defined by the add-in in its call to [ISldWorks::DefineMessageBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineMessageBar.md).

It is the add-in's responsibility to ensure that the ID is unique by using, for example, a combination of add-in module name and unique message identifier:

"MyAddInName+ID\_MYMESSAGE1"

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.md)  
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.md)
