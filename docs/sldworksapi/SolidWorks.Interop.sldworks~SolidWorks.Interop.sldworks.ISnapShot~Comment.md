# Comment Property (ISnapShot)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot~Comment`

Gets or sets the comment on this snapshot.
Gets or sets the comment on this snapshot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Comment As System.String
```

```

Dim instance As ISnapShot
Dim value As System.String
 
instance.Comment = value
 
value = instance.Comment
```

```

System.string Comment {get; set;}
```

```

property System.String^ Comment {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Comment (see **Remarks**)

Remarks

To add a time stamp to the comment, prepend the comment string with "<TS>".

For example:

       snap1.Comment = "<TS> This is a comment for SnapShot1"

generates:

       07/29/2011 04:08 PM  *user\_id*:   This is a comment for SnapShot1

Example

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)  
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)  
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISnapShot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.md)  
[ISnapShot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.md)
